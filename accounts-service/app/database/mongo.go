package database

import (
	"context"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"log"
	"time"
)

var collection *mongo.Collection

// Init is a function that initializes the database connection
func Init() {
	opts := options.Client().ApplyURI("mongodb://mongoadmin:P%40ssw0rd@localhost:27017/?authSource=admin")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	client, err := mongo.Connect(ctx, opts)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	err = client.Ping(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}

	collection = client.Database("acc_meta").Collection("metadata")
}

// GetCollection is a function that return the database collection
func GetCollection() *mongo.Collection {
	return collection
}
