object Main {
    def main(args: Array[String]): Unit = {
        val numbers = scala.io.StdIn.readLine().split(" ")
        val a = numbers(0).toInt
        val b = numbers(1).toInt
        println(a + b)
    }
}