# ETS Pull

A simple interface for accessing the ETS GRE and TOEFL server-to-server APIs.


## Usage
To use a service, create an instance of the service you want to use:

```python
from ets_pull import GREService
gre = GREService('username', 'password')
data = gre.getScoreLinkData(start_dt, end_dt)
```
    
For each service, ETS provides three interfaces:

- **getScoreLinkData**: Fetch data reported to your institution from a specific range (`start_dt`, `end_dt`) of test dates.
- **getScoreLinkDataByReportDate**: Fetch data reported to your institution from a specific range (`start_dt`, `end_dt`) of report dates.
- **getEDIData**: Fetch data for a specific range (`start_dt`, `end_dt`) of test dates that will be delivered in EDI format.

## Consuming the Data
An easy way to work with the data is with Pandas. This package provides layout files that makes it easy to read your test scores into a dataframe.

```Python
import datetime as dt
import io
import pandas as pd
import GREService


start_dt = dt.datetime(2018,1,1)
end_dt = dt.datetime(2018,1,14)

# pull data
gre = GREService('username', 'password')
gre_data = gre.getScoreLinkData(start_dt, end_dt)

# `gre_data` now contains your data as a string. You can save the raw data 
# to file or convert it into a file-like object in memory, like below:
data_obj = io.StringIO(gre_data)

# read layout into its own dataframe and use it to read the gre data
layout = pd.read_csv('path/to/gre_layout.csv')
df = pd.read_fwf(data_obj, widths=layout.width, names=layout.field_name)
```


For more information see the [ETS documentation](https://www.ets.org/portal/scores-server/).
