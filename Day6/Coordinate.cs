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

		public Coordinate(Point point, int closestDistance, int closestLocation)
		{
			this.point = point;
			ClosestDistance = closestDistance;
			LocationID = closestLocation;
		}

    }
}
