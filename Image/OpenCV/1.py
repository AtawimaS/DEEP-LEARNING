import cv2
import time

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    
    # Cek apakah kamera berhasil terbuka
    if not cam.isOpened():
        print("Error: Kamera tidak bisa dibuka.")
        exit()

    prev_frame_time = 0
    new_frame_time = 0

    while True:
        success, frame = cam.read()
        if success:
            new_frame_time = time.time()
            
            # Hitung FPS
            fps = 1 / (new_frame_time - prev_frame_time)
            prev_frame_time = new_frame_time
            
            # Tampilkan FPS di frame
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            # Tampilkan frame
            cv2.imshow("video", frame)

            # Tekan 'q' untuk keluar dari loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Gagal mengambil frame.")
            break

    cam.release()
    cv2.destroyAllWindows()
