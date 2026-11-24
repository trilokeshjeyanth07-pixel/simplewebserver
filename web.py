from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
    <title>Laptop Details</title>
</head>

<body bgcolor="white">
<h1>lokesh(26007595)</h1>

    <h1 align="center">LAPTOP DETAILS</h1>


    <table border="1" align="center" cellpadding="" width="100">

        <tr>
            <th><font color="black">S.No.</font></th>
            <th><font color="black">Device Name</font></th>
            <th><font color="black">processor</font></th>
            <th><font color="black">Installed RAM</font></th>
            <th><font color="black">Graphics Card</font></th>
            <th><font color="black">storage</font></th>
        
        </tr>
        
        <tr>
            <td><font color="black">1</font></td>
            <td><font color="black">Acer</font></td>
            <td><font color="black">Intel Core i5</font></td>
            <td><font color="black">16GB</font></td>
            <td><font color="black">Integrated card</font></td>
            <td><font color="black">512</font></td>
        </tr>
        <tr>
    <td><font color="black">2</font></td>
    <td><font color="black">HP</font></td>
    <td><font color="black">Intel Core i5</font></td>
    <td><font color="black">8GB</font></td>
    <td><font color="black">Integrated card</font></td>
    <td><font color="black">512</font></td>
</tr>

<tr>
    <td><font color="black">3</font></td>
    <td><font color="black">Dell</font></td>
    <td><font color="black">Intel Core i7</font></td>
    <td><font color="black">16GB</font></td>
    <td><font color="black">NVIDIA</font></td>
    <td><font color="black">1TB</font></td>
</tr>

<tr>
    <td><font color="black">4</font></td>
    <td><font color="black">Lenovo</font></td>
    <td><font color="black">Ryzen 5</font></td>
    <td><font color="black">8GB</font></td>
    <td><font color="black">Integrated card</font></td>
    <td><font color="black">512</font></td>
</tr>

<tr>
    <td><font color="black">5</font></td>
    <td><font color="black">Asus</font></td>
    <td><font color="black">Intel Core i7</font></td>
    <td><font color="black">16GB</font></td>
    <td><font color="black">NVIDIA</font></td>
    <td><font color="black">1TB</font></td>
</tr>
    </table>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
