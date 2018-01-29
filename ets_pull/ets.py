import datetime as dt
import zeep
from zeep.wsse.username import UsernameToken
from .exceptions import AuthenticationError


def parse_response(response):
    """
    Parse a response from one of the services. 
    
    If no data is returned, return None.
    If an error message is given, raise the appropriate exception.
    If data is returned, decode the bytes to string.
    """
    if response is None:
        return None
    
    response_str = response.decode()
    if response_str.endswith('Please check your username, password.'):
        raise AuthenticationError(response_str.strip())
    elif response_str.startswith('Logon failure'):
        raise AuthenticationError(response_str.strip())
    else:
        return response_str


class AbstractScoreManager(object):
    
    WSDL_URL = ''
    DT_FORMAT = '%m/%d/%Y'
    
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._user_token = UsernameToken(username, password)
        self.client = zeep.Client(self.WSDL_URL, wsse=self._user_token)
        
        
    def getScoreLinkData(self, start_dt, end_dt):
        """
        Fetch test scores by test date for given date range.
        
        Args:
            start_dt (datetime): The start date for the date range query.
            end_dt (datetime): The end date for the date range query.
        Returns:
            str: Test data in fixed-width format.
            
            The test data follows the standard fixed-width layout for the test
            as specified by ETS.
        """
        if end_dt < start_dt:
            raise ValueError('end_dt cannot be less than start_dt.')
        start_dt_str = start_dt.strftime(self.DT_FORMAT)
        end_dt_str = end_dt.strftime(self.DT_FORMAT)
        data = {
            'userName': self._username,
            'password': self._password,
            'teststartdate': start_dt_str,
            'testenddate': end_dt_str
        }
        response = self.client.service.getScorelinkData(**data)
        return parse_response(response)
        
        
    def getEDIData(self, start_dt, end_dt):
        if end_dt < start_dt:
            raise ValueError('end_dt cannot be less than start_dt.')
        start_dt_str = start_dt.strftime(self.DT_FORMAT)
        end_dt_str = end_dt.strftime(self.DT_FORMAT)
        data = {
            'userName': self._username,
            'password': self._password,
            'teststartdate': start_dt_str,
            'testenddate': end_dt_str
        }
        response = self.client.service.getEDIData(**data)
        return parse_response(response)


    def getScorelinkDataByReportDate(self, start_dt, end_dt):
        if end_dt < start_dt:
            raise ValueError('end_dt cannot be less than start_dt.')
        start_dt_str = start_dt.strftime(self.DT_FORMAT)
        end_dt_str = end_dt.strftime(self.DT_FORMAT)
        data = {
            'userName': self._username,
            'password': self._password,
            'reportstartdate': start_dt_str,
            'reportenddate': end_dt_str
        }
        response = self.client.service.getScorelinkDataByReportDate(**data)
        return parse_response(response)
        
        
class TOEFLService(AbstractScoreManager):
    
    WSDL_URL = 'https://datamanager.ets.org/TOEFLWebService/TOEFLEdm.wsdl'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GREService(AbstractScoreManager):
    
    WSDL_URL = 'https://datamanager.ets.org/GREWebService/GREEdm.wsdl'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

