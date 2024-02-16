namespace FizzBuzz.Tests;

using Xunit;

public class FizzBuzzTests
{
    const string ExpectedFizzBuzz = "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16";

    [Fact]
    public void WritesCorrectOutputForCount()
    {
        // Arrange
        int count = 16;
        string expected = ExpectedFizzBuzz;

        var writer = new StringWriter();
        Console.SetOut(writer);

        // Act
        Program.Main([$"{count}"]);

        // Assert        
        Assert.Equal(expected, writer.GetStringBuilder().ToString().Trim());
    }
}