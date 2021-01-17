package main

import (
	"account-metadata-service/app/api"
	"account-metadata-service/app/database"
	"github.com/gin-gonic/gin"
	"net/http"
)

func rootHandler(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"detail": "Account Metadata Service"})
}

func main() {
	database.Init()

	r := gin.Default()

	r.GET("/", rootHandler)
	r.GET("/metadata", api.GetAccountMeta())
	r.POST("/metadata", api.CreateAccountMeta())

	r.Run(":5001")
}
