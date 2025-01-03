import { SvelteMap } from 'svelte/reactivity';

const modals = ['auth'] as const;
type IModals = (typeof modals)[number];

const modals_state = $state(new SvelteMap<IModals, boolean>(modals.map((item) => [item, false])));

export function get_modals_state() {
	return modals_state;
}

export function open_modal(modal: IModals) {
	// close all modals first
	modals_state.keys().forEach((key) => {
		modals_state.set(key, false);
	});
	modals_state.set(modal, true);
}

export function close_modal(modal: IModals) {
	modals_state.set(modal, false);
}
