package main

import "testing"

func TestFibonacci(t *testing.T) {
	testCases := [][]int{
		{0, 1},
		{1, 1},
		{2, 2},
		{3, 3},
		{4, 5},
		{5, 8},
	}
	for _, testCase := range testCases {
		value, err := fibonacci(testCase[0])
		if err != nil {
			t.Error("Unable to compute fibonacci sequence. Errors from the fiboannci function.", err.Error())
		}
		if value != testCase[1]  {
			t.Error("Wrong value equated from fibonacci logic. Expected:", testCase[1], "Obtained", value)
		}
	}
}