from client import EnterpriseSemanticKernelPluginConnectorClient

def main():
    client = EnterpriseSemanticKernelPluginConnectorClient()
    res = client.bridge_native_plugin_with_planner('Banking_Wire_Transfer_Authentication_Plugin', 8)
    print('Kernel Binding: ' + res['kernel_binding_id'] + ' | ' + res['plugin_name'])
    print('Functions: ' + str(res['functions_registered']) + ' | Vector Memory: ' + str(res['semantic_memory_vector_connected']))
    print('Planner Ready: ' + str(res['stepwise_planner_plan_generated']) + ' (Safety Pass: ' + str(res['execution_safety_policy_passed']) + ')')
    print('OpenAPI Spec: ' + res['openapi_spec_export_url'])

if __name__ == '__main__':
    main()
