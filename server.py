import websocket

#It turned out to be impossible to wrap the connection code into the HTML, inline JS is not sufficient
#So we'll use websockets for the connection, and manage them from here