<script>
	import AboutIcon from '../Icons/AboutIcon.svelte';
	import Filter from '../Icons/FilterIcon.svelte';
	import HelpIcon from '../Icons/HelpIcon.svelte';
	import PlusCircle from '../Icons/PlusCircle.svelte';
	import User from '../User/User.svelte';

	const YEAR = new Date().getFullYear();
</script>

<div class="bg-base-300 fixed mt-[75px] h-screen w-[300px] pr-4">
	<div class="ml-4 py-6">
		<!-- Filter and Create -->
		<div class="mb-3 py-2">
			<h1 class="text-base-content mb-3 text-xl font-[600]">Communities</h1>
			<div class="">
				<label class="input bg-base-300 input-bordered flex h-[40px] items-center pl-0">
					<input
						type="text"
						class="input w-ful grow placeholder:text-base placeholder:font-bold focus:border-none"
						placeholder="Filter"
					/>
					<Filter />
				</label>
			</div>

			<span class="text-base-content mt-3 flex cursor-pointer space-x-2 text-xs font-[500]">
				<PlusCircle />
				<span>Create Communities</span>
			</span>
		</div>
		<!-- Favourite -->
		<div class="w-full">
			<h1 class="text-base-content/50 font-[500]">Favourites</h1>
			<div class="py-3">
				<User img="" name="danish" stared={true} />
				<User
					img="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
					name="suneeth"
					stared={true}
				/>
			</div>
		</div>
		<!-- Your Communities -->
		<div class="w-full">
			<h1 class="text-base-content/50 font-[500]">Your Communities</h1>
			<div class="py-3">
				<User img="" name="staff" stared={false} />
				<User
					img="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp"
					name="john"
					stared={false}
				/>
			</div>
		</div>
		<!-- Resources -->
		<div class="">
			<h1 class="text-base-content/50 font-[500]">Resources</h1>
			<div class="flex flex-col gap-2 py-3">
				<span class="flex cursor-pointer items-center space-x-2">
					<AboutIcon />
					<span class="text-base font-[600]">About Quibble</span>
				</span>
				<span class="flex cursor-pointer items-center space-x-2">
					<HelpIcon />
					<span class="text-base font-bold">Help</span>
				</span>
			</div>
		</div>

		<p class="mt-5 text-[10px] font-[400]">Quibble © {YEAR}. All rights reserved.</p>
	</div>
</div>
