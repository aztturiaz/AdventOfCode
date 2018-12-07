﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace Day6
{
	class Program
	{
		static void Main(string[] args)
		{
			Dictionary<int, Point> data;
			data = Day6Data.data;
			data = Day6Data.testData;

			Console.WriteLine(string.Format("Max Value in Data = {0},{1}", data.Values.Max(p => p.X), data.Values.Max(p => p.Y)));
			Console.WriteLine(string.Format("Min Value in Data = {0},{1}", data.Values.Min(p => p.X), data.Values.Min(p => p.Y)));

			Point minBoundary = new Point(data.Values.Min(p => p.X), data.Values.Min(p => p.Y));
			Point maxBoundary = new Point(data.Values.Max(p => p.X), data.Values.Max(p => p.Y));

			Console.WriteLine(string.Format("Manhattan Distance between {0} and {1} = {2}", minBoundary, maxBoundary, minBoundary.ManhattanDistance(maxBoundary)));

			if (data.ContainsKey(10))
			{
				Console.WriteLine("Contains Key!");
			}
			if (data.ContainsValue(minBoundary))
			{
				Console.WriteLine(string.Format("Contains Value = {0}", minBoundary));
			}
			
			//int[,] matrix = new int[(maxBoundary.X + 1) - minBoundary.X, (maxBoundary.Y + 1) - minBoundary.Y];
			int[,] matrix = new int[(maxBoundary.Y + 1) - minBoundary.Y, (maxBoundary.X + 1) - minBoundary.X];

			for (int x = minBoundary.X; x <= maxBoundary.X; x++)
			{
				for (int y = minBoundary.Y; y < maxBoundary.Y; y++)
				{
					Point origin = new Point(x, y);
					if (data.ContainsValue(origin))
					{
						//matrix[x - 1, y - 1] = data.FirstOrDefault(d => d.Value.Equals(origin)).Key * 10;
						matrix[y - 1, x - 1] = data.FirstOrDefault(d => d.Value.Equals(origin)).Key * 10;
						break;
					}
					
					int closestDistance = 0;
					foreach (Point destiny in data.Values)
					{
						if (closestDistance == 0 || origin.ManhattanDistance(destiny) < closestDistance)
						{
							closestDistance = origin.ManhattanDistance(destiny);
							//matrix[x - 1, y - 1] = matrix[x - 1, y - 1] > 0 || matrix[x - 1, y - 1] == -1 ? -1 : data.FirstOrDefault(d => d.Value.Equals(destiny)).Key;
							matrix[y - 1, x - 1] = matrix[y - 1, x - 1] > 0 || matrix[y - 1, x - 1] == -1 ? -1 : data.FirstOrDefault(d => d.Value.Equals(destiny)).Key;
						}
						
					}
				}
			}
			



			// Print matrix for TESTING
			for (int i = 0; i < matrix.GetLength(1); i++)
			{
				string s = string.Empty;

				for (int j = 0; j < matrix.GetLength(0); j++)
				{
					s += string.Format("\t{0}", matrix[j, i].ToString());
				}
				Console.WriteLine(s);
			}

			Console.ReadLine();

		}
	}
}
