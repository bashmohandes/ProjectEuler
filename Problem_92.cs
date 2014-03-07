static class IntExtensions
{
	static Dictionary<int, bool> cache = new Dictionary<int, bool>();
	public static bool EndsIn89(this int start)
	{
		int d = start;
		while(true)
		{
			bool b;
			if(cache.TryGetValue(d, out b))
			{
				cache[d] = b;
				return b;
			}
			d = NextNumberInChain(d);
		}	
	}
	
	static IntExtensions() 
	{
		cache.Add(1, false);
		cache.Add(89, true);
	}
	
	static int NextNumberInChain(int start)
	{
		int tmp = start;
		int result = 0;
		while(tmp > 0)
		{
			int r = tmp % 10;
			result += r * r;
			tmp /= 10;
		}
		return result;
	}
}

void Main()
{
	Console.WriteLine(
		Enumerable.Range(1, 10000000).Count(e => e.EndsIn89())
		);
}


