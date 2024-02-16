# MobTraining

This is a simple app to be used in a mob programming exercise.
It is used when playing [MOB PROGRAMMING: THE ROLEPLAYING GAME](https://github.com/willemlarsen/mobprogrammingrpg/blob/master/README.md).

> NOTE: All applications and tests are setup as a skeletons only. Tests were added in a red state and will need to be modified, verify whether the assertions are correct or whether you need to add new tests

## Goal

Goals of the exercise are:
- Learn how mob programming works by completing the FizzBuzz kata
- Learn how to work together in a mob
- Learn how to apply TDD in a mob

## The FizzBuzz kata

Create a solution that generates output matching the pattern of `1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16` up to a given number. e.g `1` for number 1, `1, 2` for number 2, `1, 2, Fizz` for number 3 etc.

If you complete the kata too quickly you can expand it with the following additional requirements:
- Pass divisor arguments on which to fizz or buzz: fizz_buzz(100, {fizz: 3, buzz: 4})
- Pass any number of divisor arguments: fizz_buzz(100, {fizz: 3, buzz: 4, foo: 8, bar: 9})
- Create a FizzBuzz cuckoo clock that accepts a time in 24-hour format (fizz_buzz_cuckoo("16:15")) and returns "Fizz," "Buzz," or "FizzBuzz" if the minute portion is evenly divisible, "Cuckoo" if the time is on a half hour, or as many "Cuckoos" as needed for the top of the hour e.g. 6 if given "06:00" or "18:00".

## Getting started

Clone the repository and build it.

```console
git clone https://github.com/robbiekouwenberg/MobTraining
```

**Flavors**

To provide teams the least amount of effort in learning a new programming language we provide some example starters. If you're feeling adventurous you are encouraged to pick a language you are unfamiliar with.

### dotnet

This is a .NET 8 console application with a xUnit test project

```
dotnet
│   MobTraining.sln
│
├───FizzBuzz
│       FizzBuzz.csproj
│       FizzBuzzer.cs
│       Program.cs
│
└───FizzBuzz.Tests
        FizzBuzz.Tests.csproj
        FizzBuzzTests.cs
```

Hints:
- Running the application 
> ```console
> dotnet run
> ```

- Running the tests manually

> ```console
> dotnet test
> ```

- Running the tests (watch mode)

> ```console
> dotnet watch test --project .\FizzBuzz.Tests\
> ```

### Python

This is a python console application with supporting tests using pytest and pytest-watch

```
python
├───fizz_buzz.py
└───tests.py
```

#### Dependencies
To install dependent packages:
```console
pip install -r requirements.txt
```

Hints:
- Running the application 
> ```console
> python fizz_buzz.py
> ```

- Running the tests manually
> ```console
> pytest
> ```

- Running the tests (watch mode)
> ```console
> ptw
> ```

### Java

This is a Java console application with supporting tests using junit.

> Note: the author knows barely anything about java. improvements are appreciated.

```
│───run.cmd
│───test.cmd
│
├───.vscode
│   └───settings.json
│
├───lib
│   └───junit-platform-console-standalone-1.10.2.jar
│
└───src
    ├───App.java
    ├───FizzBuzzer.java
    └───FizzBuzzerTest.java
```

Hints:
- Running the application 
> ```console
> run.cmd
> ```

- Running the tests manually
> ```console
> test.cmd
> ```