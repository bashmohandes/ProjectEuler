Dictionary<int, bool> cache = new Dictionary<int, bool>();
void Main()
{
	cache.Add(1, false);
	cache.Add(89, true);
	int count = 0;
	for(int i=1; i<=10000000; i++)
	{
		if(EndsIn89(i))
			count++;
	}
	
	Console.WriteLine(count);
}


int NextNumberInChain(int start)
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

bool EndsIn89(int start)
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

// Define other methods and classes here
