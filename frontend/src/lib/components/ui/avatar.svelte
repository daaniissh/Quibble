<script lang="ts">
	import { cn } from '$lib/functions/classnames';

	type Props = {
		src?: string | null;
		alt: string;
		class?: string;
		parent_class?: string;
	};

	let { src, alt, class: klass, parent_class }: Props = $props();
</script>

<div class={cn(parent_class, 'avatar')} class:placeholder={src == undefined}>
	<div class={cn(klass, 'size-6 rounded-full bg-neutral')}>
		{#if src}
			<img {src} alt="" />
		{:else}
			<span class="font-medium capitalize text-neutral-content">{alt.charAt(0)}</span>
		{/if}
	</div>
</div>
