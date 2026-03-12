;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname 005_exercise) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
(require 2htdp/image)

;; Exercise 5. Use the 2htdp/image teachpack to create the image of a simple boat or tree.
;; Make sure you can easily change the scale of the entire image.

(define SCALE 10)

(define TREE_HEIGHT (* 2 SCALE))
(define TREE_RADIUS SCALE)
(define TREE_TRUNK (/ TREE_RADIUS 2))


(overlay/xy  (circle TREE_RADIUS "solid" "green")
             (/ (- (* 2 TREE_RADIUS) TREE_TRUNK) 2) (* TREE_RADIUS 2)
(rectangle TREE_TRUNK TREE_HEIGHT "solid" "brown"))