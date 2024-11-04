using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FastEnemy : MonoBehaviour
{
    private float speed = 4.2f;

    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        // Different movement pattern: move diagonally downwards
        transform.Translate(new Vector3(1, -1, 0) * Time.deltaTime * speed);

  
        // Destroy if it goes off-screen
        if (transform.position.y < -8.5f)
        {
            Destroy(this.gameObject);
        }
    }
}
