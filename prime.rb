include Math


#エラトステネスの篩
def fetch_prime_list(max)
	search_list = (2..max).to_a
	prime_list = []
	stop_number = Math.sqrt(max).floor
	while search_list[0] <= stop_number do
		k = search_list[0]
		prime_list << k
		search_list.delete_if{|num| num % k == 0}	
	end
	return prime_list.concat(search_list)
end

p fetch_prime_list(100)
