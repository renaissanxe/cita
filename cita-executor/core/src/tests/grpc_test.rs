use cita_types::{Address, U256};
//    use core_executor::tests::helpers::{get_temp_state};
use super::helpers::*;
use evm;
use evm::action_params::{ActionParams, ActionValue};
use executive::Executive;
use grpc_contracts::contract::{contract_creation_address, low_contract_address};
use grpc_contracts::service_registry;
use util::BytesRef;

mod grpc_service {
    //use contracts::permission_management::contains_resource;
    use grpc::{RequestOptions, Server, ServerBuilder, SingleResponse};
    use libproto::citacode::{InvokeRequest, InvokeResponse};
    use libproto::citacode_grpc::{
        CitacodeService as GRPCVMService, CitacodeServiceClient as GRPCVMServiceClient,
        CitacodeServiceServer as GRPCVMServiceServer,
    };
    use std::str;
    use std::sync::{Arc, Mutex};

    pub struct GRPCVMServiceImpl {
        init_count: Arc<Mutex<u8>>,
    }

    impl GRPCVMService for GRPCVMServiceImpl {
        fn init(&self, _o: RequestOptions, _p: InvokeRequest) -> SingleResponse<InvokeResponse> {
            let mut count = self.init_count.lock().unwrap();
            *count += 1;
            let mut response = InvokeResponse::new();
            response.set_message((*count).to_string());
            SingleResponse::completed(response)
        }

        fn invoke(&self, _o: RequestOptions, p: InvokeRequest) -> SingleResponse<InvokeResponse> {
            let param = p.param.into_option().unwrap();
            let command = str::from_utf8(&(param.data)).unwrap();
            let return_value: String = match command {
                "inc" => {
                    let mut count = self.init_count.lock().unwrap();
                    *count += 1;
                    (*count).to_string()
                }
                "count" => {
                    let mut count = self.init_count.lock().unwrap();
                    (*count).to_string()
                }
                "hello" => "hello".to_string(),
                _ => {
                    error!("unknown request {:}", command);
                    "".to_string()
                }
            };
            let mut response = InvokeResponse::new();
            response.set_message(return_value);
            SingleResponse::completed(response)
        }
    }

    impl GRPCVMServiceImpl {
        pub fn new() -> Self {
            GRPCVMServiceImpl {
                init_count: Arc::new(Mutex::new(0)),
            }
        }
    }

    pub fn vm_grpc_server(port: u16) -> Option<Server> {
        let mut server = ServerBuilder::new_plain();
        server.http.set_port(port);
        server.add_service(GRPCVMServiceServer::new_service_def(
            GRPCVMServiceImpl::new(),
        ));
        //    server.http.set_cpu_pool_threads(1);
        match server.build() {
            Ok(server) => Some(server),
            Err(_) => None,
        }
    }

    pub fn vm_grpc_client(port: u16) -> GRPCVMServiceClient {
        let client_conf = Default::default();
        GRPCVMServiceClient::new_plain("::1", port, client_conf).unwrap()
    }
}

fn call_vm(params: ActionParams) -> evm::Result<evm::FinalizationResult> {
    use engines::NullEngine;
    use evm::env_info::EnvInfo;
    use evm::{Factory, VMType};
    use libexecutor::executor::EconomicalModel;
    use native::factory::Factory as NativeFactory;
    use state::Substate;
    use trace::{ExecutiveTracer, ExecutiveVMTracer};
    let factory = Factory::new(VMType::Interpreter, 1024 * 32);
    let native_factory = NativeFactory::default();
    let mut tracer = ExecutiveTracer::default();
    let mut vm_tracer = ExecutiveVMTracer::toplevel();

    let mut state = get_temp_state();
    let info = EnvInfo::default();
    let engine = NullEngine::default();
    let mut substate = Substate::new();
    let mut ex = Executive::new(
        &mut state,
        &info,
        &engine,
        &factory,
        &native_factory,
        false,
        EconomicalModel::Quota,
    );
    let mut out = vec![];
    ex.call(
        params,
        &mut substate,
        BytesRef::Fixed(&mut out),
        &mut tracer,
        &mut vm_tracer,
    )
}

#[test]
fn call_grpc_contract() {
    let server = grpc_service::vm_grpc_server(0).unwrap();
    let port = server.local_addr().port().unwrap();
    let _client = grpc_service::vm_grpc_client(port);
    let sender = Address::default();
    let address: Address = low_contract_address();
    let ip = "127.0.0.1";
    let height = 0;
    // register GRPC contract
    service_registry::register_contract(address, ip.to_string(), port, height);
    assert!(service_registry::find_contract(address, true).is_none());
    // enable GRPC contract
    let mut params = ActionParams::default();
    params.address = contract_creation_address();
    params.code_address = contract_creation_address();
    params.sender = sender.clone();
    params.origin = sender.clone();
    params.gas = U256::from(10000);
    params.value = ActionValue::Apparent(0.into());
    params.data = Some(address.to_vec());
    let _ = call_vm(params);
    assert!(service_registry::find_contract(address, true).is_some());
    // check count value
    let mut basic_params = ActionParams::default();
    basic_params.address = address;
    basic_params.code_address = address;
    basic_params.sender = sender.clone();
    basic_params.origin = sender.clone();
    basic_params.gas = U256::from(10000);
    basic_params.value = ActionValue::Apparent(0.into());

    let mut params = basic_params.clone();
    params.data = Some("count".as_bytes().to_vec());
    let result = call_vm(params);
    let value: u32 = String::from_utf8_lossy(&result.unwrap().return_data)
        .parse()
        .unwrap();
    assert_eq!(value, 1);
    // call it again
    let mut params = basic_params.clone();
    params.data = Some("inc".as_bytes().to_vec());
    let result = call_vm(params);
    let value: u32 = String::from_utf8_lossy(&result.unwrap().return_data)
        .parse()
        .unwrap();
    assert_eq!(value, 2);
}
