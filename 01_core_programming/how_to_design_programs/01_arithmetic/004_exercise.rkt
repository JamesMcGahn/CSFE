;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname 004_exercise) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
;;Exercise 4. Use the same setup as in exercise 3 to create an expression that deletes the ith
;;position from str. 
(define str "helloworld")
(define i 5)



(string-append (substring str 0 i) (substring str (+ i 1))) 