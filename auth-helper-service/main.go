package main

import (
	md "auth-helper-service/middleware"
	"github.com/gin-gonic/gin"
)

func rootHandler(c *gin.Context) {
	c.JSON(200, gin.H{"detail": "OK"})
}

func main() {
	r := gin.Default()
	r.Use(md.JWTParserMiddleware(), md.RequestIDMiddleware())
	r.GET("/", rootHandler)

	r.Run(":5000")
}
