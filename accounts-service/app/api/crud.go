package api

import (
	"account-metadata-service/app/database"
	"context"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"time"
)

var ctx, cancel = context.WithTimeout(context.Background(), 5*time.Second)
var collection = database.GetCollection()

func getAccountMetadata(userID string) {

}

func createAccountMetadata(userID string) error {
	metaObj := &database.Meta{
		ID:        primitive.NewObjectID(),
		CreatedAt: time.Now(),
		UpdatedAt: time.Now(),
		UserID:    userID,
	}

	_, err := collection.InsertOne(ctx, *metaObj)
	return err
}
