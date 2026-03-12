;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname 002_exercise) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
;;Exercise 2. Add the following two lines to the definitions area:
(define prefix "hello")
(define suffix "world")

#| Then use string primitives to create an expression that concatenates prefix and suffix and adds "_"
between them. When you run this program, you will see "hello_world" in the interactions area.
|#

(string-append prefix "_" suffix)