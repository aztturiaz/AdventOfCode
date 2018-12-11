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
			//data = Day6Data.testData2;

			Console.WriteLine(string.Format("Max Value in Data = {0},{1}", data.Values.Max(p => p.X), data.Values.Max(p => p.Y)));
			Console.WriteLine(string.Format("Min Value in Data = {0},{1}", data.Values.Min(p => p.X), data.Values.Min(p => p.Y)));

			Point minBoundary = new Point(data.Values.Min(p => p.X), data.Values.Min(p => p.Y));
			Point maxBoundary = new Point(data.Values.Max(p => p.X), data.Values.Max(p => p.Y));

			minBoundary.Offset(-1, -1);
			maxBoundary.Offset(1, 1);

			// ========================================
			Coordinate[,] matrix = new Coordinate[(maxBoundary.X - minBoundary.X) + 1, (maxBoundary.Y - minBoundary.Y) + 1];
			List<Coordinate> coordsList = new List<Coordinate>();
			// ========================================

			int col = 0;

			for (int x = minBoundary.X; x <= maxBoundary.X; x++)
			{
				int row = 0;

				for (int y = minBoundary.Y; y <= maxBoundary.Y; y++)
				{
					Point origin = new Point(x, y);
					if (data.ContainsValue(origin))
					{
						int originID = data.FirstOrDefault(d => d.Value.Equals(origin)).Key;
						matrix[col, row] = new Coordinate(origin, 0, originID);
						if (x == minBoundary.X || x == maxBoundary.X  || y == minBoundary.Y || y == maxBoundary.Y)
						{
							matrix[col, row].ExtendsToInfinty = true;
						}
						coordsList.Add(matrix[col, row]);
						row++;
						continue;
					}
					
					int manhattanDistance = 0;
					int destinyID = 0;
					foreach (Point destiny in data.Values)
					{
						manhattanDistance = origin.ManhattanDistance(destiny);
						destinyID = data.FirstOrDefault(d => d.Value.Equals(destiny)).Key;

						Coordinate coord = matrix[col, row];
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
							matrix[col, row] = new Coordinate(origin, manhattanDistance, destinyID);
							if (x == minBoundary.X || x == maxBoundary.X || y == minBoundary.Y || y == maxBoundary.Y)
							{
								matrix[col, row].ExtendsToInfinty = true;
							}
							coordsList.Add(matrix[col, row]);
						}
					}
					row++; 
				}
				col++;
			}

			// Get the area of locations non infinite extended
			var regions = from c1 in coordsList
						 join c2 in (from c in coordsList
									 where c.ExtendsToInfinty
									 group c by c.LocationID into InfinityLocations
									 select new { LocationID = InfinityLocations.Key })
							 on new { id = c1.LocationID } equals new { id = c2.LocationID } into grp
						 from cc in grp.DefaultIfEmpty()
						 where cc == null
						 group c1 by c1.LocationID into locationGroup
						 select new { LocationID = locationGroup.Key, Area = locationGroup.Sum(x => 1) };

			Console.WriteLine("\n");
			int LargestRegionArea = 0;
			foreach (var c in regions)
			{
				LargestRegionArea = c.Area > LargestRegionArea ? c.Area : LargestRegionArea;
			}

			Console.WriteLine(string.Format("Largest Area: {0}", LargestRegionArea));


			Coordinate.PrintMap(matrix);
			Console.ReadLine();

		}
	}
}
