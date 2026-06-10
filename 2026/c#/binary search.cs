using System;

class Program
{
    static void Main()
    {
        Random random = new Random();
        while (true)
        {
        Console.Write("Enter the number of random numbers to generate:\n from 1 to ");
        int numbers = int.Parse(Console.ReadLine());
        Console.WriteLine("\n\n\n");
        int steps = 0; 
        int step = 0; 
        int min = 1;
        int max = numbers;    
        int total = random.Next(1, numbers + 1);  
        step = total/2;
        while (step != total)
        {
            while (step < total)
            {
                min = step;
                step = (max + min) / 2;
                steps++;
            }
            while (step > total)
            {
                max = step;
                step = (max + min) / 2;
                steps++;
            }
        }
        Console.WriteLine("correct number: " + step);
        Console.WriteLine("Total steps: " + steps);
        }
    }
}
