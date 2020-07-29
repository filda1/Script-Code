<h2>Editar Post {{ $post_id }}</h2>

<input type="hidden" class="form-control" wire:model="post_id">
@include('livewire.form')
<button wire:click="update" class="btn btn-primary">
    Actualizar
</button>

<button wire:click="default" class="btn btn=link">
    Cancelar
</button>
