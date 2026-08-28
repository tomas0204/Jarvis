#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .setup(|app| {
            if cfg!(debug_assertions) {
                app.handle().plugin(
                    tauri_plugin_log::Builder::default()
                        .level(log::LevelFilter::Info)
                        .build(),
                )?;
            }

            #[cfg(debug_assertions)]
            {
                use std::process::Command;

                let project_root = std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR"))
                    .join("../..");

                let python = project_root.join(".venv/Scripts/python.exe");

                Command::new(python)
                    .args([
                        "-m",
                        "uvicorn",
                        "backend.api.app:app",
                    ])
                    .current_dir(&project_root)
                    .spawn()
                    .expect("No se pudo iniciar el backend de Jarvis");
            }

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}