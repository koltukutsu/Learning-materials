package main

import (
	"fmt"
	"os"
	"bufio"
	"log"
	"strings"
)

func main() {
	taboo_words := make(map[string]struct{})
	var file_name string
	fmt.Scanf("%s", &file_name)
	
	file, err := os.Open(file_name)

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)

	for scanner.Scan(){
		key := string(scanner.Text())
		key = strings.ToLower(key)
		taboo_words[key] = struct{}{}
	}

	total_out:
	for {
		reader := bufio.NewReader(os.Stdin)
		user_sentence, _ := reader.ReadString('\n')
		user_words := strings.Fields(user_sentence)

		for j, word := range user_words {
			// if j == 0{
			// 	fmt.Println()
			// }

			word_lower := strings.ToLower(word)

			if strings.Compare(word_lower, "exit") == 0 {
				fmt.Println("Bye!")
				break total_out
			}

			if _, ok := taboo_words[word_lower]; ok {
				length := len(word_lower)
				replacement := ""
				
				for i := 0; i < length; i++ {
					replacement += "*"
				}
				switch j {
				case len(user_words) - 1:
					fmt.Print(replacement)
				default:
					fmt.Print(replacement + " ")
				}
				
			} else {
				switch j {
				case len(user_words) - 1:
					fmt.Print(word)
				default:
					fmt.Print(word + " ")
				}
			}
		}
		fmt.Println()
	}
}