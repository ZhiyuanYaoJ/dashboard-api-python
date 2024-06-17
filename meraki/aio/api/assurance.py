import urllib

"""
PUBLIC_API_PATH = {
    "core_assurance": {
        "authentication": {
            "mr": "{base_url}/organizations/{organization_id}/wireless/clients/connections/authentication/byClient?networkIds[]={network_id}&timespan={timespan}",
            "ms": "{base_url}/organizations/{organization_id}/switch/clients/connections/authentication/byClient?networkIds[]={network_id}&timespan={timespan}",
            "mx": "{base_url}/organizations/{organization_id}/appliance/vpn/remoteAccess/secureClient/authentication/byClient?networkIds[]={network_id}&timespan={timespan}",
        },
        "association": {
            "mr": "{base_url}/organizations/{organization_id}/wireless/clients/connections/association/byClient?networkIds[]={network_id}&timespan={timespan}",
        },
        "ip": {
            "mr": "{base_url}/organizations/{organization_id}/wireless/clients/connections/dhcp/byClient?networkIds[]={network_id}&timespan={timespan}",
            "ms": "{base_url}/organizations/{organization_id}/switch/clients/connections/dhcp/byClient?networkIds[]={network_id}&timespan={timespan}",
            "mx": "{base_url}/organizations/{organization_id}/appliance/vpn/remoteAccess/secureClient/ipAssignment/byClient?networkIds[]={network_id}&timespan={timespan}",
        },
        "vpn": {
            "mx": "{base_url}/organizations/{organization_id}/appliance/vpn/remoteAccess/secureClient/tunnelCreation/byClient?networkIds[]={network_id}&timespan={timespan}"
        },
        "score": {
            "all": "{base_url}/organizations/{organization_id}/assurance/scores?networkIds[]={network_id}&timespan={timespan}",
        }
    }
}


"""

class AsyncAssurance(object):
    """
    This class contains APIs for full-stack assurance (Sentinel) functionality. By the time of writing, these APIs are in beta and are subject to change.
    """

    def __init__(self, session):
        super().__init__()
        self._session = session

    def getAssuranceScore(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **Return the overall health score for the organization**
        "{base_url}/organizations/{organization_id}/assurance/scores?networkIds[]={network_id}&timespan={timespan}"

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'scores'],
            'operation': 'getAssuranceScore'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/assurance/scores'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)

    
    def getClientAuthMR(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the authentication failures for wireless clients**
        "{base_url}/organizations/{organization_id}/wireless/clients/connections/authentication/byClient?networkIds[]={network_id}&timespan={timespan}",

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'wireless', 'clients', 'authentication'],
            'operation': 'getClientAuthMR'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/clients/connections/authentication/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
    
    def getClientAuthMS(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the authentication failures for clients connected to switches**
        "{base_url}/organizations/{organization_id}/switch/clients/connections/authentication/byClient?networkIds[]={network_id}&timespan={timespan}",

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'switch', 'clients', 'authentication'],
            'operation': 'getClientAuthMS'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/switch/clients/connections/authentication/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
    
    def getClientAuthMX(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the authentication failures for clients connected to MX**
        "{base_url}/organizations/{organization_id}/appliance/vpn/remoteAccess/secureClient/authentication/byClient?networkIds[]={network_id}&timespan={timespan}",

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'vpn', 'clients', 'authentication'],
            'operation': 'getClientAuthMX'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/remoteAccess/secureClient/authentication/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
    
    def getClientAssocMR(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the association failures for wireless clients**
        "{base_url}/organizations/{organization_id}/wireless/clients/connections/association/byClient?networkIds[]={network_id}&timespan={timespan}",

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'wireless', 'clients', 'association'],
            'operation': 'getClientAssocMR'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/clients/connections/association/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
    

    def getClientIpMR(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the DHCP failures for wireless clients**
        "{base_url}/organizations/{organization_id}/wireless/clients/connections/dhcp/byClient?networkIds[]={network_id}&timespan={timespan}",

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'wireless', 'clients', 'dhcp'],
            'operation': 'getClientIpMR'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/clients/connections/dhcp/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
    
    def getClientIpMS(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the dhcp failures for clients connected to switches**
        "{base_url}/organizations/{organization_id}/switch/clients/connections/dhcp/byClient?networkIds[]={network_id}&timespan={timespan}",

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'switch', 'clients', 'dhcp'],
            'operation': 'getClientIpMS'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/switch/clients/connections/dhcp/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
    
    def getClientIpMX(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the dhcp failures for clients connected to MX**
        "{base_url}/organizations/{organization_id}/appliance/vpn/remoteAccess/secureClient/dhcp/byClient?networkIds[]={network_id}&timespan={timespan}",

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'vpn', 'clients', 'dhcp'],
            'operation': 'getClientIpMX'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/remoteAccess/secureClient/dhcp/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
    
    def getClientTunnelCreation(self, organizationId: str, networkIds: list, timespan: int, **kwargs):
        """
        **List the VPN tunnel creation failures for clients connected to MX**
        "{base_url}/organizations/{organization_id}/appliance/vpn/remoteAccess/secureClient/tunnelCreation/byClient?networkIds[]={network_id}&timespan={timespan}"

        - organizationId (string): Organization ID
        - networkIds (array): A list of network IDs to include
        - timespan (integer): The timespan for the data. Must be a multiple of 600 and at most 1 day.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 week from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 week after t0.
        """
        
        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'assurance', 'vpn', 'clients', 'tunnel'],
            'operation': 'getClientTunnelCreation'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/remoteAccess/secureClient/tunnelCreation/byClient'

        query_params = ['networkIds', 'timespan', 't0', 't1', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, _ in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)