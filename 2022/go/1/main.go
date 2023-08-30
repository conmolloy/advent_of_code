package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	filePath := "input.txt"

	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error reading file")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	temp := 0
	Rslice := []int{} 

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			if temp > 0 && (len(Rslice) < 3 || temp > Rslice[len(Rslice)-1]) {
				Rslice = append(Rslice, temp)
				sort.Sort(sort.Reverse(sort.IntSlice(Rslice)))
				if len(Rslice) > 3 {
					Rslice = Rslice[:3]
				}
			}
			temp = 0
		} else {
			val, err := strconv.Atoi(line)
			if err != nil {
				fmt.Println("Error converting to integer:", err)
				return
			}
			temp += val
		}
	}

	fmt.Println("The top three are:")
	fmt.Println(Rslice)

	sum := 0
	for _, num := range Rslice {
		sum += num
	}
	fmt.Println("Sum of top three:", sum)
}
