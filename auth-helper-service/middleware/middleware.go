package middleware

import (
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"strings"
)

// JWTParserMiddleware decodes the JWT Token passed in request headers. If a valid user object is found,
// it attaches user info to the request and allows the request to propagate. Otherwise, error 401 is raised
func JWTParserMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		token := c.Request.Header["Authorization"][0]
		if strings.Contains(token, " ") {
			jwt := strings.Split(token, " ")[1]

			// Decode token here

			c.Writer.Header().Set("X-User-Id", jwt)
			c.Next()
		} else {
			c.JSON(400, gin.H{"detail": "Improperly formatted token"})
			c.Abort()
		}
	}
}

// RequestIDMiddleware is a simple function that attaches a UUID into the request headers
func RequestIDMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		reqID := uuid.New().String()
		c.Writer.Header().Set("X-Request-Id", reqID)
		c.Next()
	}
}
