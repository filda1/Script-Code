<div class="form-group">
    <label>Título</label>
    <input type="text" class="form-control" wire:model="title">
    @error('title') <span class="text-danger">{{ $message }}</span> @enderror
</div>

<div class="form-group">
    <label>Contenido</label>
    <textarea class="form-control" wire:model="body"></textarea>
    @error('body') <span class="text-danger">{{ $message }}</span> @enderror
</div>
