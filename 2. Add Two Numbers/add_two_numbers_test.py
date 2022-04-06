import unittest

from add_two_numbers import Solution
from add_two_numbers import ListNode

class AddTwoNumbersTest(unittest.TestCase):
  def test_one(self):
    self.assertEqual(
      Solution.addTwoNumbers(
        self=None,
        l1 = ListNode(
          val = 2,
          next = ListNode(
            val = 4,
            next = ListNode(
              val = 3,
              next = None
            )
          )
        ),
        l2=ListNode(
          val = 5,
          next = ListNode(
            val = 6,
            next = ListNode(
              val = 4,
              next = None
            )
          )
        ) 
      ),

      ListNode(
        val = 7,
        next = ListNode(
          val = 0,
          next = ListNode(
            val = 8,
            next = None
          )
        )
      )

    )

  def test_two(self):
    self.assertEqual(
      Solution.addTwoNumbers(
        self=None,
        l1 = ListNode(
          val = 0,
          next = None
        ),
        l2 = ListNode(
          val = 0,
          next = None
        )
      ),
      ListNode(
        val = 0,
        next = None
      )
    )

  def test_three(self):
    self.assertEqual(
      Solution.addTwoNumbers(
        self=None,
        l1 = ListNode(
          val = 9,
          next = ListNode(
            val = 9,
            next = ListNode(
              val = 9,
              next = ListNode(
                val = 9,
                next = ListNode(
                  val = 9,
                  next = ListNode(
                    val = 9,
                    next = ListNode(
                      val = 9,
                      next = None
                    )
                  )
                )
              )
            )
          )
        ),
        l2 = ListNode(
          val = 9,
          next = ListNode(
            val = 9,
            next = ListNode(
              val = 9,
              next = ListNode(
                val = 9,
                next = None
              )
            )
          )
        )
      ),

      ListNode(
        val = 8,
        next = ListNode(
          val = 9,
          next = ListNode(
            val = 9,
            next = ListNode(
              val = 9,
              next = ListNode(
                val = 0,
                next = ListNode(
                  val = 0,
                  next = ListNode(
                    val = 0,
                    next = ListNode(
                      val = 1,
                      next = None
                    )
                  )
                )
              )
            )
          )
        )
      )

    )