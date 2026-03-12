;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname 009_exercise) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
(require 2htdp/image)

#|

Exercise 9. Add the following line to the definitions area of DrRacket:
(define in ...)

Then create an expression that converts the value of in to a non-negative number. For a String,
 it determines how long the String is; for an Image, it uses the area; for a Number, it uses the 
absolute value; for #true it uses 10 and for #false 20. 


|#


(define in (square 10 "solid" "blue"))


(define (convertin in) 
  (cond
    [(number? in) (abs in)]
    [(image? in) (* (image-width in) (image-height in))]
    [(string? in) (string-length in)]
    [(boolean? in) (if (equal? true in) 10 20)]))

(convertin in)

