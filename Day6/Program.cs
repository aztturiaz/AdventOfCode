using System;
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

			minBoundary.Offset(-1, -1);
			maxBoundary.Offset(1, 1);

			Console.WriteLine(string.Format("Manhattan Distance between {0} and {1} = {2}", minBoundary, maxBoundary, minBoundary.ManhattanDistance(maxBoundary)));

			
			
			if (data.ContainsKey(10))
			{
				Console.WriteLine("Contains Key!");
			}
			if (data.ContainsValue(minBoundary))
			{
				Console.WriteLine(string.Format("Contains Value = {0}", minBoundary));
			}

			// ========================================

			//Dictionary<Point, int> coordinates = new Dictionary<Point, int>();
			Coordinate[,] matrix = new Coordinate[(maxBoundary.X + 1), (maxBoundary.Y + 1)];
			List<Coordinate> coordsList = new List<Coordinate>();

			// ========================================


			for (int x = minBoundary.X; x <= maxBoundary.X; x++)
			{
				for (int y = minBoundary.Y; y <= maxBoundary.Y; y++)
				{
					Point origin = new Point(x, y);
					if (data.ContainsValue(origin))
					{
						int originID = data.FirstOrDefault(d => d.Value.Equals(origin)).Key * 10;
						//matrix[x, y] = new Coordinate(origin, 0, originID * 10);
						matrix[x, y] = new Coordinate(origin, 0, originID);
						coordsList.Add(matrix[x, y]);
						if (x == minBoundary.X || x == maxBoundary.X  || y == minBoundary.Y || y == maxBoundary.Y 
								)//|| coordsList.Where(c => c.LocationID == originID / 10 && c.ExtendsToInfinty).Any())
						{
							matrix[x, y].ExtendsToInfinty = true;
						}
						coordsList.Add(matrix[x, y]);
						continue;
					}
					
					int manhattanDistance = 0;
					int destinyID = 0;
					foreach (Point destiny in data.Values)
					{
						manhattanDistance = origin.ManhattanDistance(destiny);
						destinyID = data.FirstOrDefault(d => d.Value.Equals(destiny)).Key;

						Coordinate coord = matrix[x, y];
						if (coord != null)
						{
							if (manhattanDistance < coord.ClosestDistance)
							{
								coord.ClosestDistance = manhattanDistance;
								coord.LocationID = destinyID;
							}
							else if (manhattanDistance == coord.ClosestDistance)
							{
								coord.LocationID = -1; 
							}
						}
						else
						{
							matrix[x, y] = new Coordinate(origin, manhattanDistance, destinyID);
							if (x == minBoundary.X || x == maxBoundary.X || y == minBoundary.Y || y == maxBoundary.Y
									)//|| coordsList.Where(c => c.LocationID == destinyID && c.ExtendsToInfinty).Any())
							{
								matrix[x, y].ExtendsToInfinty = true;
							}
						}
						coordsList.Add(matrix[x, y]);
					}
				}
			}



			// Print matrix for TESTING
			for (int i = 0; i < matrix.GetLength(1); i++)
			{
				string s = string.Empty;

				for (int j = 0; j < matrix.GetLength(0); j++)
				{
					if (matrix[j, i] != null)
					{
						if (matrix[j, i].ExtendsToInfinty && matrix[j,i].LocationID > 0)
						{
							s += string.Format("\t{0}", "&");
						}
						else
						{
							if (matrix[j, i].LocationID == -1)
								s += string.Format("\t.");
							else
								s += string.Format("\t{0}", matrix[j, i].LocationID);
						}						
					}					
				}
				Console.WriteLine(s);
			}

			Console.WriteLine("\n");
			foreach (var c in coordsList.Where(c => c != null && !c.ExtendsToInfinty))
			{
				Console.WriteLine(string.Format("Location ID: {0}", c.LocationID));
			}

			Console.ReadLine();

		}
	}
}
