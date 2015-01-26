mssqldos<br />
Denial of service using MS-SQL servers to amplify attacks <br />
<br />
mssqldos works by sending the [CLNT_BCAST_EX](https://msdn.microsoft.com/en-us/library/cc219743.aspx) broadcast packet which asks for a list of database instances on the network and how to connect to them. In essence mssqldos asks for the phonebook to be mailed to the target IP thousands of times per second

Usage:<br />
<b>Please consult mssqldos.py -h</b>
<br />

<b> Mitigation: </b> None at this time
<br />
[Additional material from Kurt Aubuchon](http://kurtaubuchon.blogspot.com/2015/01/mc-sqlr-amplification-ms-sql-server.html)