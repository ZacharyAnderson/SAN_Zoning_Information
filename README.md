# SAN Zoning information
This web app will allow technical staff to troubleshoot zoning information on the fly.

## Back-End
The back-end of this web application is written in python using the Flask extension.
The main back-end function is to gather information from Brocade switches using the Brocade Network Advisor(BNA) API.
We communicate with the BNA API through pythons requests library. The back-end gathers all the active zones from the zone database on the switches. We are then able to query the zone database and output our query as a JSON object. The API/route that the front-end will need to request looks like:
```
@app.route('/saninfo/api/v1.0/hostname/<host>', methods =['GET'])
def get_hostname_info(host):
    return jsonify(brocade_functions.queryZoneDB(host, zoneDB))
```

An Example of the output generated is:
```
{
    "abluex_sd0aatd0aa_testvpx0248_local_g2_copy": [
        "50:00:14:42:A0:63:22:02",
        "50:00:14:42:B0:63:22:02",
        "10:00:5A:6A:E6:50:01:C6"
    ],
    "bluex_sf01ntd0aa_mainframtest_1551_3par246c_012_212": [
        "20:12:00:02:AC:01:24:6C",
        "23:12:00:02:AC:01:24:6C",
        "C0:50:76:E0:E0:80:0F:E0"
    ],
    "redx_sf008td00k_mainframetest_1541_3par4860_011_211": [
        "20:11:00:02:AC:01:24:6C",
        "22:11:00:02:AC:01:24:6C",
        "C0:50:76:E0:E0:80:0B:E8"
    ]
}
```
Where the command used is:
```
curl -X GET \
  http://127.0.0.1:5000/saninfo/api/v1.0/hostname/test
```
