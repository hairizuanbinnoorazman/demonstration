package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type person struct {
	Id     string `json:"id"`
	Name   string `json:"name"`
	School string `json:"school"`
}

type personGet struct{}

func (p personGet) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	log.Println("Person Get Route Started")
	defer log.Println("Person Get Route Stopped")

	fakePerson := person{Id: "tester", Name: "tester name", School: "Nope, never studied"}
	encoder := json.NewEncoder(w)
	encoder.Encode(fakePerson)
}

func main() {
	log.Println("Begin server")
	http.Handle("/api/person/v1/0010", personGet{})
	log.Fatal(http.ListenAndServe(":8080", nil))
}
