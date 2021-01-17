package database

import (
	"go.mongodb.org/mongo-driver/bson/primitive"
	"time"
)

// Meta is a model blue-print for an account metadata object
type Meta struct {
	ID        primitive.ObjectID `bson:"_id"`
	UserID    string             `bson:"user_id"`
	CreatedAt time.Time          `bson:"created_at"`
	UpdatedAt time.Time          `bson:"updated_at"`
}
