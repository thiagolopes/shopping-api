package promotion

import (
	"context"
	"log"
)

type Server struct {
	UnimplementedDiscountServiceServer
}

func (s *Server) AvailableDiscounts(ctx context.Context, order *Order) (*Discounts, error) {
	log.Println(order)
	log.Println(order.User.GetDateBirth())
	return &Discounts{}, nil
}
