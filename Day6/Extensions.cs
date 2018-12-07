using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace Day6
{
    public static class Extensions
    {
		public static int ManhattanDistance(this Point origin, Point destiny)
		{
			return Math.Abs(destiny.X - origin.X) + Math.Abs(destiny.Y - origin.Y);
		}
	}
}
