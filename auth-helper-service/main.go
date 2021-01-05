package main

import (
	md "auth-helper-service/middleware"
	"github.com/gin-gonic/gin"
	"net/http"
)

func rootHandler(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"detail": "OK"})
}

func main() {
	r := gin.Default()
	r.Use(md.JWTParserMiddleware(), md.RequestIDMiddleware())
	r.GET("/", rootHandler)

	r.Run(":5000")
}
