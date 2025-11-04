# EvolutionOfHTTP
Exploring each stage of the HyperText Transfer Protocol (HTTP) to build a deeper understanding of how it works.

### Notes for me
Using existing protocols TCP and IP
  HTML (Text format to display hypertext documents)
  Protocol to exchange them(HTTP)
  A client to display these documents(the first web browser called WorldWideWeb)
  A server to give access to these documents

## HTTP/0.9 the one-line protocol
only 1 method **GET** followed by resource path
Full url wasn't included since the protocol, server and port wern't needed once connected to the server

### Example
GET /my-page.html

**Response**
<html>
  A text-only web page
</html>

### Notable missing in this version
- no headers
- no status or error codes

## HTTP/1.0 Building extensibility
### NEW
- versioning added within each request
- status code at the beginning of the response
- headers for requests and responses (used for metadata)
- Now other content types could be transmitted instead of plain HTML with **Content-Type** being added in the header

### Example
GET /my-page.html HTTP/1.0
User-Agent: NCSA_Mosaic/2.0 (Windows 3.1)

HTTP/1.0 200 OK
Date: Tue, 15 Nov 1994 08:12:31 GMT
Server: CERN/3.0 libwww/2.17
Content-Type: text/html
<HTML>
A page with an image
  <IMG SRC="/my-image.gif">
</HTML>

Now, since we have /my-image.gif this means a second connection and request is needed to fetch the image

Would look like:

GET /my-image.gif HTTP/1.0
User-Agent: NCSA_Mosaic/2.0 (Windows 3.1)

HTTP/1.0 200 OK
Date: Tue, 15 Nov 1994 08:12:32 GMT
Server: CERN/3.0 libwww/2.17
Content-Type: text/gif
(image content)

### Problems
Interoperability(def from google: the ability of different systems, applications, or organizations to work together, exchange, and use information seamlessly and securely) was widespread. 

That's why, to solve this, an informational document was created that described common practices. https://datatracker.ietf.org/doc/html/rfc1945

## HTTP/1.1 The standardized protocol
This was the first standardized version of HTTP

### Improvements
- Now could reuse a connection instead of a new one each time
- Added pipelining. Was able to send a second request before the answer of the first one was fully transmitted.
- Added chunked responses support
-  this means instead of sending the entire response in one large response the server sends it in chunks
#### Example
HTTP/1.1 200 OK
Transfer-Encoding: chunked

7
Mozilla
9
Developer
7
Network
0

Every chunk start with the size of that chunk (in hex)
followed by data
then ends with 0 to signify that it is done

Browser reassembles these chunks as they arrive so the user starts seeing the content sooner.
- more cache control mechanisms were introduced
- Content negotiation (language, encoding and type) introduced. Client and server could now agree on which content to exchange
- Host header tells the server which domain it's trying to reach
-   Server collocation(means multiple different websites can be hosted on the same physical server and share the same IP address)

### Example (One TCP reused for)
GET /en-US/docs/ HTTP/1.1
Host: developer.mozilla.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:141.0) Gecko/20100101 Firefox/141.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br, zstd
Connection: keep-alive

HTTP/1.1 200 OK
accept-ranges: none
content-encoding: br
date: Tue, 01 Jul 2025 08:32:50 GMT
expires: Tue, 01 Jul 2025 09:26:50 GMT
cache-control: public, max-age=3600
age: 1926
last-modified: Sat, 28 Jun 2025 00:47:12 GMT
etag: W/"b55394ed2f274eea5d528cf6c91e1dcf"
content-type: text/html
vary: Accept-Encoding
content-length: 26178

[26178 bytes of HTML]

GET /static/css/main.9e7d1ce5.css HTTP/1.1
Host: developer.mozilla.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:141.0) Gecko/20100101 Firefox/141.0
Accept: text/css,*/*;q=0.1
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br, zstd

HTTP/1.1 200 OK
content-encoding: br
content-length: 43694
date: Mon, 30 Jun 2025 21:13:12 GMT
expires: Mon, 30 Jun 2025 21:47:29 GMT
cache-control: public, max-age=31536000
age: 42704
last-modified: Mon, 30 Jun 2025 00:33:45 GMT
etag: W/"d4f4d0955482844ad842986a9bcb7e8a"
content-type: text/css
vary: Accept-Encoding

[43694 bytes of CSS]

GET /static/js/main.a918a4e7.js HTTP/1.1
Host: developer.mozilla.org
…




