package middleware

// JWTParserMiddleware decodes the JWT Token passed in request headers. If a valid user object is found,
// it attaches user info to the request and allows the request to propagate. Otherwise, error 401 is raised
func JWTParserMiddleware() {

}

// RequestIDMiddleware is a simple function that attaches a UUID into the request headers
func RequestIDMiddleware() {

}
