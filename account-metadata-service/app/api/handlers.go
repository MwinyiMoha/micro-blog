package api

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

// GetAccountMeta is a route handler, that given a user ID, gets metadata for that user
func GetAccountMeta() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"detail": "Retrieved"})
	}
}

// CreateAccountMeta is a route handler that creates a metadata object for a user
func CreateAccountMeta() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"detail": "Created"})
	}
}
