using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace Day6
{
	public class Coordinate
	{
		Point point;
		public int X { get{ return this.point.X; } set { point.X = value; } }
		public int Y { get{ return this.point.Y; } set { point.Y = value; } }
		public int ClosestDistance { get; set; }
		public int LocationID { get; set; }
		public bool ExtendsToInfinty { get; set; }

		public Coordinate(Point point, int closestDistance, int closestLocation)
		{
			this.point = point;
			ClosestDistance = closestDistance;
			LocationID = closestLocation;
			ExtendsToInfinty = false;
		}

		public static void PrintMap(Coordinate[,] matrix)
		{
			// Print matrix for TESTING
			for (int i = 0; i < matrix.GetLength(1); i++)
			{
				string s = string.Empty;

				for (int j = 0; j < matrix.GetLength(0); j++)
				{
					if (matrix[j, i] != null)
					{
						if (matrix[j, i].ExtendsToInfinty && matrix[j, i].LocationID > 0)
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
		}
    }
}
