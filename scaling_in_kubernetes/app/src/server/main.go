package main

import (
	"net/http"
	"time"
	"encoding/json"
	"errors"
	"log"
	"io"
	"strconv"
)

type status struct {
	Status string `json:"status"`
	ServerTime string `json:"server_time"`
}

type statusHandler struct {}

func (h statusHandler) ServeHTTP (w http.ResponseWriter, r *http.Request){
	currentTime := time.Now()
	currentTimeString := currentTime.Format(http.TimeFormat)
	statusValues := status{Status:"Ok", ServerTime:currentTimeString}

	encoder := json.NewEncoder(w)
	encoder.Encode(statusValues)
}

type fibonacciHandler struct {}

func (h fibonacciHandler) ServeHTTP (w http.ResponseWriter, r *http.Request) {
	values := r.URL.Query()
	data := values["n"][0]
	intValue, err := strconv.Atoi(data)
	if err != nil {
		log.Println("Error:", err.Error(), "Value obtained:", intValue)
	}

	if intValue > 15 {
		go fibonacci(intValue)
		io.WriteString(w, "This will take a while to process")
	} else {
		fibonacciReturn, err := fibonacci(intValue)
		if err != nil {
			log.Println("Error", err.Error())
		}
		io.WriteString(w, strconv.Itoa(fibonacciReturn))
	}
}

func fibonacci(n int) (int, error) {
	// Fibonacci is a well understood problem of how a problem can be broken down to atomical units.
	// End results of fibonacci relies on previous results.
	// Expected values: 1, 1, 2, 3, 5, 8...
	log.Println("Start of the fibonacci function")
	defer log.Println("End of the fiboanacci function")

	if n < 0 {
		return -1, errors.New("Fiboanacci function cannot take a value less than 2")
	}
	if n == 0 || n == 1 {
		return 1, nil
	}
	if n > 25 {
		return -1, errors.New("This is a test service with no optimization in place.")
	}
	firstValue, err := fibonacci(n-1)
	if err != nil {
		return -1, err
	}
	secondValue, err := fibonacci(n-2)
	if err != nil {
		return -1, err
	}
	value := firstValue + secondValue
	return value, nil
}


func main() {
	log.Println("Start Server")

	http.Handle("/", statusHandler{})
	http.Handle("/fibonacci", fibonacciHandler{})
	log.Fatal(http.ListenAndServe(":3000", nil))
}
