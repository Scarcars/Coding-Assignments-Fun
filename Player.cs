using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    // its access level: public or private
    // its type: int (5, 8, 36, etc.), float (2.5f, 3.7f, etc.)
    // its name: speed, playerSpeed --- Speed, PlayerSpeed
    // optional: give it an initial value
    private float speed;
    private int lives = 3;
    private int score = 0;
    private float horizontalInput;
    private float verticalInput;
    public GameObject bullet;

    // Start is called before the first frame update
    void Start()
    {
        speed = 5f;
    }

    // Update is called once per frame
    void Update()
    {
        Movement();
        Shooting();
    }

    void Movement()
    {
        horizontalInput = Input.GetAxis("Horizontal");
        verticalInput = Input.GetAxis("Vertical");

        // Calculate the new position
        Vector3 newPosition = transform.position + new Vector3(horizontalInput, verticalInput, 0) * Time.deltaTime * speed;
          if (newPosition.y > 0)
        {
            newPosition.y = 0; // Stop moving after middle
        }
        else if (newPosition.y < -5)
        {
            newPosition.y = -5; // Stop moving from the bottom.
        }
        
        // Wrap around the left and right edges
        if (newPosition.x > 11.5f)
        {
            newPosition.x = -11.5f;
        }
        else if (newPosition.x < -11.5f)
        {
            newPosition.x = 11.5f;
        }

        // Update the player's position
        transform.position = newPosition;
    }

    void Shooting()
    {
        // If I press SPACE
        // Create a bullet
        if (Input.GetKeyDown(KeyCode.Space))
        {
            // Create a bullet
            Instantiate(bullet, transform.position + new Vector3(0, 1, 0), Quaternion.identity);
        }
    }
}
