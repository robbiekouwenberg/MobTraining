using Xunit;

public class FizzBuzzTests
{
    [Fact]
    public void WritesCorrectOutputForCount1()
    {     
        Assert.Equal("1", new FizzBuzzer().FizzBuzz(1));
    }

    [Fact]
    public void WritesCorrectOutputForCount16()
    {     
        Assert.Equal("1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16", new FizzBuzzer().FizzBuzz(1));
    }
}